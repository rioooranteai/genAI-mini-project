import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load API Key
load_dotenv()

def text_generator(media_type: str, job: str, category: str, temperature: float):
    temperature = temperature / 10

    # Inisialisasi model LLM dengan API Key langsung
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=temperature)

    # Template untuk pesan
    prompt_template_message = PromptTemplate(
        input_variables=["job", "category", "media_type"],
        template="""Pagi ini rasanya waktu yang sempurna untuk lanjut tidur.
        Namun, saya perlu memberikan alasan yang masuk akal untuk izin tidak masuk kerja.
        Buatkan saya alasan yang lucu dan absurd, seolah-olah saya seorang komedian legendaris
        yang bisa membuat atasan yang paling serius pun tersenyum. Ingat, posisi saya adalah {job},
        jadi alasan yang diberikan harus relevan dan membahas tentang {category}, tapi tetap menghibur!
        Alasan ini akan dikirimkan melalui {media_type}."""
    )

    message_chain = LLMChain(llm=llm, prompt=prompt_template_message, output_key="message")


    if media_type == "Email":
        prompt_template_subject = PromptTemplate(
            input_variables=["job"],
            template="Buat subject email untuk pesan izin tidak masuk kantor untuk departemen {job}"
        )

        subject_chain = LLMChain(llm=llm, prompt=prompt_template_subject, output_key="email_subject")

        # Eksekusi kedua LLMChain secara independen
        subject = subject_chain.run({"job": job})
        message = message_chain.run({"job": job, "category": category, "media_type": media_type})

        return {"email_subject": subject, "message": message}

    else:
        # Untuk Chat WA, Tele, dan App pesan  chat lainnya
        message = message_chain.run({"job": job, "category": category, "media_type": media_type})
        return {"message": message}
