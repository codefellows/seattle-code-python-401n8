export default function QuestionForm({ questionAskedHandler }) {
    return (
        <form
            className="flex p-2 mx-auto my-4 bg-gray-200"
            onSubmit={questionAskedHandler}
        >
            <input name="question" className="flex-auto" />
            <button className="px-2 py-1 bg-gray-50">Ask</button>
        </form>
    );
}

// export default function QuestionForm(props) {
//   return (
//     <form
//       className="flex p-2 mx-auto my-4 bg-gray-200"
//       onSubmit={props.questionAskedHandler}
//     >
//       <input name="question" className="flex-auto" />
//       <button className="px-2 py-1 bg-gray-50">Ask</button>
//     </form>
//   );
// }
