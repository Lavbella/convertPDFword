import streamlit as st
from pdf2docx import Converter
import os
import tempfile

# Configuração da página
st.set_page_config(page_title="Conversor PDF para Word", page_icon="📝", layout="centered")

st.title("📝 Conversor de PDF para Word")
st.write("Converta os seus PDFs de volta para documentos Word (.docx) mantendo texto, tabelas e imagens.")

# Upload do ficheiro
uploaded_file = st.file_uploader("Escolha o ficheiro PDF", type=["pdf"])

if uploaded_file is not None:
    st.success("Ficheiro carregado com sucesso!")
    
    if st.button("Processar e Converter para Word"):
        with st.spinner("A converter o documento... Isto pode demorar dependendo do tamanho do PDF."):
            try:
                # Criar ficheiros temporários para processar em disco de forma segura
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                    temp_pdf.write(uploaded_file.read())
                    temp_pdf_path = temp_pdf.name
                
                # Definir o caminho de saída para o Word
                temp_docx_path = temp_pdf_path.replace(".pdf", ".docx")
                
                # Executar a conversão usando pdf2docx
                cv = Converter(temp_pdf_path)
                cv.convert(temp_docx_path, start=0, end=None)  # Converte todas as páginas
                cv.close()
                
                # Ler o ficheiro Word gerado para enviar ao utilizador
                with open(temp_docx_path, "rb") as f:
                    docx_data = f.read()
                
                st.write("---")
                st.subheader("Conversão Concluída!")
                
                # Botão para download
                st.download_button(
                    label="📥 Descarregar Documento Word",
                    data=docx_data,
                    file_name=uploaded_file.name.replace(".pdf", ".docx"),
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
                
                # Limpar os ficheiros temporários do sistema
                os.remove(temp_pdf_path)
                os.remove(temp_docx_path)
                
            except Exception as e:
                st.error(f"Ocorreu um erro durante a conversão: {e}")
