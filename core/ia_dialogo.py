# core/ia_dialogo.py

from transformers import AutoModelForCausalLM, AutoTokenizer  # , pipeline
# from transformers import pipeline
import torch

# Este era el intento anterior usando pipeline (NO BORRAR, útil para futuros equipos con micrófono)
# modelo = pipeline("conversational", model="microsoft/DialoGPT-small")

# Carga un modelo de conversación (puedes cambiarlo luego por uno más avanzado)
# chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# def responder_mensaje(mensaje):
#     from transformers import Conversation
#     conversacion = Conversation(mensaje)
#     resultado = chatbot(conversacion)
#     return str(resultado.generated_responses[-1])

# Versión actual compatible sin usar pipeline
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
modelo = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

# Historial de conversación para mantener contexto
historial_chat = []

def responder_mensaje(mensaje_usuario):
    global historial_chat

    # Codificar mensaje del usuario
    entrada_usuario = tokenizer.encode(mensaje_usuario + tokenizer.eos_token, return_tensors="pt")
    
    # Añadir al historial (últimos 5 mensajes para evitar que se vuelva demasiado largo)
    historial_chat.append(entrada_usuario)
    entrada = torch.cat(historial_chat[-5:], dim=-1)

    # Crear attention_mask para evitar advertencias del modelo
    attention_mask = entrada.ne(tokenizer.eos_token_id).long()

    # Generar respuesta
    respuesta_ids = modelo.generate(
        entrada,
        attention_mask=attention_mask,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decodificar y guardar respuesta
    respuesta = tokenizer.decode(respuesta_ids[:, entrada.shape[-1]:][0], skip_special_tokens=True)
    historial_chat.append(respuesta_ids)
    return respuesta

# Ejemplo de uso
# mensaje_usuario = "Hola, ¿cómo estás?"
# respuesta = responder_mensaje(mensaje_usuario)