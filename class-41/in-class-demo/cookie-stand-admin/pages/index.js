import Head from 'next/head';
import { useState } from 'react';
import { useAuth } from '@/contexts/auth';
import useResource from '@/hooks/useResource';

export default function Home() {
  const { login, user, logout, register, error } = useAuth();

  return (
    <div>
      <Head>
        <title>Cookie Stand Admin</title>
        <link rel='icon' href='/favicon.ico' />
      </Head>
      <header className='p-4 space-y-8 text-center text-4xl'>
        {user ? (
          <div>
            <h1>Cookie Stand Admin</h1>
            <h2 className='text-2xl'>Welcome {user.username}</h2>
            <button onClick={logout}>Logout</button>
          </div>
        ) : (
          <h1>Please Log In to Access Admin Page</h1>
        )}
      </header>

      <main>
        {user ? (
          <CookieStandAdmin />
        ) : (
          <>
            <LoginForm login={login} />
            <RegisterForm onRegister={register} error={error} />
          </>
        )}
      </main>
    </div>
  );
}

function LoginForm({ login }) {
  async function handleSubmit(event) {
    event.preventDefault();
    login(event.target.username.value, event.target.password.value);
  }

  return (
    <form onSubmit={handleSubmit} className='w-1/4 mx-auto border p-4'>
      <fieldset className='flex flex-col py-2' autoComplete='off'>
        <legend className='text-xl'>Log In</legend>
        <label htmlFor='username'>Username</label>
        <input type='text' name='username' className='border bg-lime-200' />
        <label htmlFor='password'>Password</label>
        <input type='password' name='password' className='border bg-lime-200' />
        <button type='submit' className='my-4 bg-lime-800'>
          Log In
        </button>
      </fieldset>
    </form>
  );
}

// New
function RegisterForm({ onRegister, error }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [email, setEmail] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setErrorMessage('Passwords do not match');
      return;
    }
    // pass the form values of username, password, and email to `register` in auth.js
    onRegister(username, password, email);
  };

  return (
    <form onSubmit={handleSubmit} className='flex flex-col w-2/4 mx-auto'>
      <legend className='block text-gray-700 text-lg font-bold mb-2'>
        Register New User
      </legend>
      <label className='font-bold text-gray-700 mb-2' htmlFor='username'>
        Username
      </label>
      <input
        id='username'
        type='text'
        placeholder='Username'
        onChange={(e) => setUsername(e.target.value)}
        className='p-2 mb-4 border border-gray-300 rounded shadow-sm focus:outline-none focus:border-blue-300'
      />

      <label className='font-bold text-gray-700 mb-2' htmlFor='password'>
        Password
      </label>
      <input
        id='password'
        type='password'
        placeholder='Password'
        onChange={(e) => setPassword(e.target.value)}
        className='p-2 mb-4 border border-gray-300 rounded shadow-sm focus:outline-none focus:border-blue-300'
      />

      <label className='font-bold text-gray-700 mb-2' htmlFor='confirmPassword'>
        Confirm Password
      </label>
      <input
        id='confirmPassword'
        type='password'
        placeholder='Confirm Password'
        onChange={(e) => setConfirmPassword(e.target.value)}
        className='p-2 mb-4 border border-gray-300 rounded shadow-sm focus:outline-none focus:border-blue-300'
      />

      <label className='font-bold text-gray-700 mb-2' htmlFor='email'>
        Email
      </label>
      <input
        id='email'
        type='email'
        placeholder='Email'
        onChange={(e) => setEmail(e.target.value)}
        className='p-2 mb-4 border border-gray-300 rounded shadow-sm focus:outline-none focus:border-blue-300'
      />

      {errorMessage && <p className='text-red-500'>{errorMessage}</p>}
      {/* TODO: change the `error.email` to work with any error */}
      {error && <p className='text-red-500'>{error.email}</p>}
      <button
        type='submit'
        className='mt-4 bg-blue-500 text-white p-2 rounded hover:bg-blue-400'
      >
        Register
      </button>
    </form>
  );
}

function CookieStandAdmin() {
  // resources is an array of cookie stands from our API (uses SWR)
  const { resources, deleteResource } = useResource();

  return (
    <>
      <CookieStandForm />
      <CookieStandTable stands={resources || []} deleteStand={deleteResource} />
    </>
  );
}

function CookieStandForm() {
  const { user } = useAuth();
  const { createResource } = useResource();

  function handleSubmit(event) {
    event.preventDefault();
    const info = {
      location: event.target.location.value,
      minimum_customers_per_hour: parseInt(event.target.minimum.value),
      maximum_customers_per_hour: parseInt(event.target.maximum.value),
      average_cookies_per_sale: parseFloat(event.target.average.value),
      owner: user.id,
    };
    createResource(info);
  }

  return (
    <form onSubmit={handleSubmit}>
      <fieldset>
        <legend>Create Cookie Stand</legend>
        <input placeholder='location' name='location' />
        <input placeholder='minimum' name='minimum' />
        <input placeholder='maximum' name='maximum' />
        <input placeholder='average' name='average' />
        <button>create</button>
      </fieldset>
    </form>
  );
}

function CookieStandTable({ stands, deleteStand }) {
  return (
    <table className='my-8'>
      <thead>
        <tr>
          <th>Location</th>
          <th>6 am</th>
          <th>7 am</th>
          <th>8 am</th>
          <th>9 am</th>
          <th>10 am</th>
          <th>11 am</th>
          <th>12 pm</th>
          <th>1 pm</th>
          <th>2 pm</th>
          <th>3 pm</th>
          <th>4 pm</th>
          <th>5 pm</th>
          <th>6 pm</th>
          <th>7 pm</th>
          <th>totals</th>
        </tr>
      </thead>
      <tbody>
        {stands.map((stand) => (
          <CookieStandRow
            key={stand.id}
            info={stand}
            deleteStand={deleteStand}
          />
        ))}
      </tbody>
    </table>
  );
}

function CookieStandRow({ info, deleteStand }) {
  function clickHandler() {
    deleteStand(info.id);
  }

  if (info.hourly_sales.length == 0) {
    // bunk data
    info.hourly_sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  }

  return (
    <tr>
      <td>
        {info.location} <button onClick={clickHandler}>[x]</button>
      </td>
      {info.hourly_sales.map((slot, index) => (
        <td key={index}>{slot}</td>
      ))}
      <td>{info.hourly_sales.reduce((num, sum) => num + sum, 0)}</td>
    </tr>
  );
}
