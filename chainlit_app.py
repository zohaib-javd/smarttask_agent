import chainlit as cl
from agent import run_task_agent

@cl.on_chat_start
async def start():
    await cl.Message(content="🧠 Ready to break down your task—shoot!").send()

@cl.on_message
async def on_msg(msg: cl.Message):
    reply = run_task_agent(msg.content)
    await cl.Message(content=reply).send()
