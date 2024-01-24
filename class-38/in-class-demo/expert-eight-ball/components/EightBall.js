export default function EightBall({ questionResponses }) {
  return (
    <>
      {/* {questionResponses.length > 0 ? (
        <div className='w-96 h-96 my-4 bg-salmon-cookie-pink rounded-full'>
          <div className='relative flex items-center justify-center w-48 h-48 top-16 left-16 bg-gray-50 rounded-full'>
            <p className='text-xl'>
              {questionResponses[questionResponses.length - 1].answer}
            </p>
          </div>
        </div>
      ) : (
        <div className='w-96 h-96 my-4 bg-salmon-cookie-pink rounded-full'>
          <div className='relative flex items-center justify-center w-48 h-48 top-16 left-16 bg-gray-50 rounded-full'>
            <p className='text-xl'>
              Ask a Question
            </p>
          </div>
        </div>
      )} */}
      <div className='w-96 h-96 my-4 bg-salmon-cookie-pink rounded-full'>
        <div className='relative flex items-center justify-center w-48 h-48 top-16 left-16 bg-gray-50 rounded-full'>
          <p className='text-xl'>
            {questionResponses.length > 0
              ? questionResponses[questionResponses.length - 1].response
              : 'Ask a Question'}
          </p>
        </div>
      </div>
    </>
  );
}
