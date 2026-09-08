# convertPDFword
A Python application built with Streamlit to convert PDF files into editable Word documents (.docx). Fully configured for standalone executable generation using PyInstaller, following best-practice deployment templates from my other public repositories.

# 📄 PDF to Word Converter / Conversor de PDF para Word

[Português](#português) | [English](#english)

---

## Português

Uma aplicação em Python desenvolvida com **Streamlit** concebida para converter ficheiros PDF em documentos editáveis do Word (`.docx`). O projeto está totalmente estruturado para ser convertido num executável autónomo.

### Funcionalidades
* **Conversão de Formato:** Converte documentos PDF diretamente para ficheiros Word editáveis.
* **Preservação de Texto:** Mantém a estrutura de texto original do documento de entrada.
* **Pronto para Executável:** Inclui os ficheiros de configuração necessários para compilar a app com o PyInstaller.

### Estrutura do Projeto
* `app.py`: Código principal da aplicação Streamlit.
* `run_app.py`: Script de bootstrap/inicialização para o executável.
* `run_app.spec`: Ficheiro de configuração e especificação do PyInstaller.
* `requirements.txt`: Lista de dependências para criar o ambiente Python.
* `commands.txt` / `comandos.txt`: Ficheiro de texto utilitário com os comandos necessários para o projeto.

### Como Executar Localmente
1. Crie e ative o seu ambiente virtual:
   ```bash
   python -m venv env
   # No Windows: .\env\Scripts\activate
   # No macOS/Linux: source env/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Inicie a aplicação:
   ```bash
   streamlit run app.py
   ```

### Como Criar o Executável
Para compilar a aplicação e gerar o executável final através do PyInstaller, utilize as instruções presentes no seu ficheiro de comandos ou execute:
```bash
pyinstaller --clean run_app.spec
```
O executável final independente ficará disponível na pasta `dist/`.

### 🔗 Exemplos de Referência
A arquitetura de empacotamento utilizada neste repositório (configuração do ficheiro `run_app.spec` e o script de bootstrap `run_app.py`) segue o mesmo modelo de sucesso implementado em **outros projetos públicos disponíveis no meu perfil do GitHub**. Pode consultar esses repositórios como guia para implementações semelhantes.

---

## English

A Python application built with **Streamlit** designed to convert PDF files into editable Word documents (`.docx`). The project is fully configured for standalone executable deployment.

### Features
* **Format Conversion:** Converts PDF documents directly into editable Word files.
* **Text Preservation:** Maintains the original text structure of the input document.
* **Executable Ready:** Includes all required configuration templates for compiling with PyInstaller.

### Project Structure
* `app.py`: Main Streamlit application source code.
* `run_app.py`: Bootstrap/entry-point script for the standalone executable.
* `run_app.spec`: PyInstaller configuration and specification file.
* `requirements.txt`: Python environment dependency list.
* `commands.txt`: Reference file containing all useful CLI deployment commands.

### How to Run Locally
1. Create and activate your virtual environment:
   ```bash
   python -m venv env
   # On Windows: .\env\Scripts\activate
   # On macOS/Linux: source env/bin/activate
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the application:
   ```bash
   streamlit run app.py
   ```

### How to Build the Executable
To compile the application into a standalone executable using PyInstaller, refer to your commands file or run the following command in your terminal:
```bash
pyinstaller --clean run_app.spec
```
The final standalone bundle will be generated inside the `dist/` directory.

### Reference Examples
The packaging workflow utilized in this repository (the configuration of the `run_app.spec` file and the `run_app.py` bootstrap script) follows the exact same model tested and deployed across **other public projects available on my GitHub profile**. You can explore those repositories for additional hands-on examples.
