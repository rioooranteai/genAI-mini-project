Technical Report: Absurd Excuse Generator Status Proyek Saat Ini 

Saat ini, proyek sedang dalam tahap pengembangan fitur baru untuk memungkinkan pengguna memilih bahasa dalam pembuatan alasan izin kerja yang lucu. Fokus utama meliputi:

Penambahan Fitur Pemilihan Bahasa

Mengintegrasikan opsi bahasa ke dalam UI menggunakan Streamlit. Memodifikasi prompt untuk mendukung berbagai bahasa. Menyesuaikan pipeline LLM agar dapat menghasilkan alasan dalam bahasa yang dipilih. 

Peningkatan Responsivitas Model

Mengoptimalkan prompt agar lebih sesuai dengan karakter humor di berbagai budaya. Menguji hasil pada beberapa bahasa untuk memastikan kualitas alasan tetap terjaga. 1. Overview 

Proyek ini bertujuan untuk menghasilkan alasan izin kerja yang lucu dan absurd menggunakan model bahasa dari OpenAI yang diintegrasikan dengan LangChain dan Streamlit. Pengguna dapat memilih profesi, kategori alasan, media pengiriman, serta bahasa, sehingga alasan yang dihasilkan lebih relevan dan sesuai dengan konteks pengguna.

2. Motivation 

Banyak pekerja sering mengalami situasi di mana mereka membutuhkan alasan untuk tidak masuk kerja, tetapi ingin tetap terlihat kreatif dan menghibur. Dengan adanya fitur ini, pengguna dapat membuat alasan yang unik, relevan, dan disesuaikan dengan profesi mereka dalam berbagai bahasa.

Penambahan fitur pemilihan bahasa bertujuan untuk memperluas jangkauan pengguna serta memastikan bahwa alasan yang dihasilkan tetap lucu dan kontekstual dalam berbagai bahasa dan budaya.

3. Success Metrics Kualitas Humor: Diukur berdasarkan feedback pengguna terhadap alasan yang dihasilkan. Relevansi Alasan: Alasan harus sesuai dengan profesi dan kategori yang dipilih. Keakuratan Bahasa: Alasan yang dihasilkan sesuai dengan bahasa yang dipilih oleh pengguna. Waktu Respons: Maksimal 3 detik untuk menghasilkan alasan setelah pengguna melakukan input. 4. Requirements & Constraints 4.1 Functional Requirements Pemilihan Bahasa: Pengguna dapat memilih bahasa untuk alasan izin. Penyesuaian Prompt: Prompt akan diadaptasi agar humor tetap sesuai dengan bahasa yang dipilih. Generasi Teks: Menggunakan OpenAI API melalui LangChain untuk menghasilkan alasan izin. Integrasi Streamlit: UI memungkinkan pengguna memilih profesi, kategori alasan, media pengiriman, dan bahasa. 4.2 Constraints Dukungan Bahasa: Awalnya akan mendukung Bahasa Indonesia dan Inggris, dengan potensi penambahan bahasa lain. Batasan Model: Kualitas humor dapat bervariasi tergantung pada bahasa yang dipilih. Waktu Respons: Harus dioptimalkan agar tidak melebihi 3 detik. 4.3 What's In-Scope & Out-of-Scope 

In-Scope:
✔ Menambahkan fitur pemilihan bahasa dalam UI.
✔ Menyesuaikan prompt agar sesuai dengan bahasa yang dipilih.

Out-of-Scope:
✘ Penerjemahan otomatis alasan ke berbagai bahasa setelah dihasilkan.
✘ Penggunaan model lokal selain OpenAI API.

5. Methodology 5.1 Problem Statement 

Masalah ini diformulasikan sebagai natural language generation (NLG) di mana model harus menghasilkan teks yang sesuai dengan konteks pengguna berdasarkan beberapa parameter yang dipilih.

5.2 Data Sumber Data: OpenAI API dengan fine-tuned prompt. Input: Profesi, kategori alasan, media pengiriman, dan bahasa. Output: Alasan izin kerja yang lucu dan relevan dalam bahasa yang dipilih. 5.3 Techniques Model Language: OpenAI GPT-4 via LangChain. Prompt Engineering: Template disesuaikan untuk setiap bahasa yang didukung. Menggunakan variabel {job}, {category}, {media_type}, dan {language} dalam prompt. Integrasi UI: Menggunakan Streamlit untuk mempermudah pemilihan parameter oleh pengguna. 6. Results and Analysis 

Proses pengujian awal menunjukkan bahwa alasan yang dihasilkan cukup menghibur dalam Bahasa Indonesia dan Inggris. Namun, diperlukan optimasi lebih lanjut agar humor tetap sesuai dengan budaya masing-masing bahasa.

7. Conclusion 

Proyek ini memungkinkan pengguna untuk menghasilkan alasan izin kerja yang lucu dan absurd dengan fleksibilitas tambahan dalam pemilihan bahasa. Dengan optimasi prompt dan integrasi UI yang lebih baik, proyek ini dapat menjadi alat hiburan yang lebih luas dan lebih kontekstual di berbagai negara.


