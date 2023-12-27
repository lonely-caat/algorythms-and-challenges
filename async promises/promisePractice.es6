// Advanced Promises Usage in JavaScript

// 1. Sequential Execution of an Array of Promises
function executePromisesSequentially(promises) {
    return promises.reduce((promiseChain, currentPromise) => {
        return promiseChain.then(chainResults =>
            currentPromise.then(currentResult => [...chainResults, currentResult])
        );
    }, Promise.resolve([]));
}

// 2. Throttling Promise Execution (Run N promises at a time)
function throttlePromises(promises, maxConcurrent) {
    let executing = promises.splice(0, maxConcurrent);
    let processNext = function() {
        if (promises.length > 0) {
            let nextPromise = promises.shift();
            nextPromise.then(processNext);
            executing.push(nextPromise);
            executing = executing.filter(p => p !== nextPromise);
        }
    };
    executing.forEach(p => p.then(processNext));
    return Promise.all(executing);
}

// 3. Retrying a Promise until it Resolves
function retryPromise(promiseFunc, maxAttempts) {
    function attempt(n) {
        return promiseFunc().catch(error => {
            if (n === 1) throw error;
            return attempt(n - 1);
        });
    }
    return attempt(maxAttempts);
}

// 4. Wrapping Callback Function to Return a Promise
function promisify(callbackBasedApi) {
    return function(...args) {
        return new Promise((resolve, reject) => {
            callbackBasedApi(...args, (err, result) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(result);
                }
            });
        });
    };
}

// 5. Implementing a Simple Delay Function Using Promises
function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}

