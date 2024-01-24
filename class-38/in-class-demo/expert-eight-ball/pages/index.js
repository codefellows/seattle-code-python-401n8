import Head from 'next/head';
import { replies } from '../data';
import { useState } from 'react';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import QuestionForm from '@/components/QuestionForm';
import EightBall from '@/components/EightBall';
import ResponseTable from '@/components/ResponseTable';

export default function Home() {
  const [questionResponses, setQuestionResponses] = useState([]);

  function questionResponseHandler(event) {
    event.preventDefault();

    // get a random reply from replies
    const randomReply = replies[Math.floor(Math.random() * replies.length)];

    // represent the Question and Response as an object
    const questionResponse = {
      question: event.target.question.value, // comes from the input
      response: randomReply,
    };

    // setReply(randomReply);
    setQuestionResponses([...questionResponses, questionResponse]); // like pushing a new into state
  }

  return (
    <div>
      <Head>
        <title>Expert Eight Ball</title>
        <link rel='icon' href='/favicon.ico' />
      </Head>

      <Header questionResponses={questionResponses} />

      <main className='flex flex-col items-center py-4'>
        {/* Question Form */}
        <QuestionForm questionAskedHandler={questionResponseHandler} />

        {/* Eight Ball */}
        <EightBall questionResponses={questionResponses} />

        {/* Response Table */}
        <ResponseTable questionResponses={questionResponses} />
      </main>

      <Footer />
    </div>
  );
}
