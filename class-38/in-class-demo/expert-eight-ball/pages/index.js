import Head from "next/head";
import { replies } from "../data";
import { useState } from "react";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import QuestionForm from "@/components/QuestionForm";
import EightBall from "@/components/EightBall";

export default function Home() {
    const [reply, setReply] = useState("Ask me something");

    function questionAskedHandler(event) {
        event.preventDefault();

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

            <Header />

            <main className="flex flex-col items-center py-4">
                {/* Question Form */}
                <QuestionForm questionAskedHandler={questionAskedHandler} />

                {/* Eight Ball */}
                <EightBall reply={reply} />
            </main>

            <Footer />
        </div>
    );
}
