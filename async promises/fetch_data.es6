function fetchAndProcessData(url1, url2) {
  return fetchData(url1)
    .then(data => processData(data))
    .then(() => fetchData(url2))
    .then(data => processData(data))
    .catch(error => console.error('An error occurred:', error));
}


async function fetchAndProcessDataAsync(url) {
  try {
    const data = await fetchData(url);
    const processedData = await processData(data);
    return processedData;
  } catch (error) {
    console.error('An error occurred:', error);
  }
}


function fetchMultipleUrls(urls) {
  const promises = urls.map(url => fetchData(url));
  return Promise.all(promises)
    .then(results => {
      console.log('All data fetched', results);
      return results;
    })
    .catch(error => console.error('Error in fetching:', error));
}

//Promise.race is used when you need only the first resolved promise among many. It's useful for timeout patterns or getting the fastest result from multiple sources.
function fetchDataWithTimeout(url, timeout) {
  const fetchDataPromise = fetchData(url);
  const timeoutPromise = new Promise((_, reject) => setTimeout(() => reject(new Error('Request timed out')), timeout));
  return Promise.race([fetchDataPromise, timeoutPromise]);
}
