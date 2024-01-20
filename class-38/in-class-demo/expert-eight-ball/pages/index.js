import Head from "next/head";
import Link from "next/link";
import { replies } from "../data";
import { useState } from "react";

export default function Home() {
  const [reply, setReply] = useState("Ask me something");

  function questionAskedHandler(event) {
    event.preventDefault();
    // alert(event.target.question.value);

    // get a random reply from replies
    const randomReply = replies[Math.floor(Math.random() * replies.length)];
    setReply(randomReply);

  }

  return (
    <div>
      <Head>
        <title>Expert Eight Ball</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <header className="flex items-center justify-between p-5 bg-gray-500 text-gray-50">
        <h1 className="text-4xl">Expert Eight Ball</h1>
        <p>1 question answered</p>
      </header>

      <main className="flex flex-col items-center py-4">
        {/* Question Form */}
        <form
          className="flex p-2 mx-auto my-4 bg-gray-200"
          onSubmit={questionAskedHandler}
        >
          <input name="question" className="flex-auto" />
          <button className="px-2 py-1 bg-gray-50">Ask</button>
        </form>

        {/* Eight Ball */}
        <div className="w-96 h-96 my-4 bg-gray-900 rounded-full">
          <div className="relative flex items-center justify-center w-48 h-48 top-16 left-16 bg-gray-50 rounded-full">
            <p className="text-xl">{reply}</p>
          </div>
        </div>
      </main>

      <footer className="flex justify-between p-4 mt-8 bg-gray-500 text-gray-50">
        <p>Expert Eight Ball &copy;2024</p>
        <Link href="/careers">
          Careers
        </Link>
      </footer>
    </div>
  );
}
