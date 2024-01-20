export default function EightBall({ reply }) {
    return (
        <div className="w-96 h-96 my-4 bg-salmon-cookie-pink rounded-full">
            <div className="relative flex items-center justify-center w-48 h-48 top-16 left-16 bg-gray-50 rounded-full">
                <p className="text-xl">{reply}</p>
            </div>
        </div>
    );
}
