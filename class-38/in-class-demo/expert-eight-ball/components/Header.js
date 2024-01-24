export default function Header({ questionResponses }) {
  return (
    <header className='flex items-center justify-between p-5 bg-gray-500 text-gray-50'>
      <h1 className='text-4xl'>Expert Eight Ball</h1>
      <p>Questions Answered {questionResponses.length}</p>
    </header>
  );
}
