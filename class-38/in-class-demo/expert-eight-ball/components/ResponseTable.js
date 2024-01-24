export default function ResponseTable({ questionResponses }) {
  return (
    <>
      {questionResponses.length > 0 && (
        <table className='w-1/2 border-2 border-gray-500'>
          <thead>
            <tr>
              <th className='h-8 border-2 border-gray-500'>Question</th>
              <th className='h-8 border-2 border-gray-500'>Response</th>
            </tr>
          </thead>
          <tbody>
            {/* questionResponses is an array of object literals */}
            {questionResponses.map((item, idx) => {
              return (
                <tr key={idx}>
                  <td className='h-8 text-center border-2 border-gray-500'>
                    {item.question}
                  </td>
                  <td className='h-8 text-center border-2 border-gray-500'>
                    {item.response}
                  </td>
                </tr>
              );
            })}
          </tbody>

          {/* TODO: Footer contains the most common response */}
          {/* <tfoot>

        </tfoot> */}
        </table>
      )}
    </>
  );
}
