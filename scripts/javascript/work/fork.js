process.on("message", message => {
  console.log("收到父进程的消息:", message)
  process.send({ result: "Hello from child process!" })
})
