// 在主线程中使用 worker.onmessage，在 Worker 中使用 self.onmessage。
self.onmessage = event => {
  const data = event.data
  const result = data * 2
  self.postMessage(result)
  // throw new Error('Something went wrong!');
}
