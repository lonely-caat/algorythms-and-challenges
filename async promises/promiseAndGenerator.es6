function* fetchSequentially(urls) {
  for (const url of urls) {
    try {
      const data = yield fetchData(url);
      console.log(`Data from ${url}:`, data);
    } catch (error) {
      console.error(`Error fetching ${url}:`, error);
    }
  }
}

function executeGenerator(genFunc) {
  const generator = genFunc();

  function handle(yielded) {
    if (!yielded.done) {
      yielded.value.then(result => handle(generator.next(result)))
        .catch(error => handle(generator.throw(error)));
    }
  }

  handle(generator.next());
}

//executeGenerator(() => fetchSequentially(arrayOfUrls))
