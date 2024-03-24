from setuptools import setup, find_packages
setup(name='Generative-AI-Project', version='1.0', packages=find_packages(),
    install_requires=['Openai', 'langchain', 'streamlit', 'python-dotenv', 'PyPDF2'],
    python_requires=">=3.8",
    author='Robert',
    author_email='rssebambulidde@gmail.com',
    description='Generative AI Project',
    long_description_content_type="text/markdown")