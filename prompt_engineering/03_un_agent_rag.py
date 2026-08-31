import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# 1. Configuration de la clé API OpenAI
os.environ["OPENAI_API_KEY"] = "votre-cle-api-openai"

# 2. Vos documents internes (La base de connaissances)
documents_source = [
    Document(page_content="La politique de télétravail de l'entreprise autorise jusqu'à 2 jours par semaine après validation du manager."),
    Document(page_content="Les notes de frais de transport doivent être soumises avant le 25 de chaque mois sur l'application interne."),
    Document(page_content="Le mot de passe du réseau Wi-Fi invité est 'WelcomeToTech2026' et change tous les lundis matins.")
]

# 3. Initialisation du modèle d'embedding (Vectorisation)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# 4. Création et alimentation de la base de données vectorielle (en mémoire)
vector_store = Chroma.from_documents(documents_source, embeddings)

# 5. Configuration du moteur de recherche (Retrieval)
# On configure le moteur pour chercher les 2 documents les plus pertinents (k=2)
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 6. Définition du modèle de langage (LLM) et du Prompt
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

system_prompt = (
    "Tu es un assistant RH. Réponds à la question uniquement en utilisant le contexte fourni.\n"
    "Si tu ne connais pas la réponse, dis simplement 'Je ne sais pas'.\n\n"
    "Contexte :\n{context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# 7. Assemblage de la chaîne RAG
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# 8. Test du système RAG
question = "Comment se passe le télétravail chez nous ?"
response = rag_chain.invoke({"input": question})

print(f"Question : {question}")
print(f"Réponse  : {response['answer']}")
