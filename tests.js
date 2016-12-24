const tests = [
  () => 1 + 1 === 2,
  () => 'a' + 'b' === 'ab'
]

function runTest(test) {
  try {
    return test()
  }
  catch (e) {
    console.error('Test failed', e)
    return false
  }
}

const passingTests = tests.filter(runTest)
if (tests.length === passingTests.length) {
  console.log('All tests passed')
}
else {
  console.error('Some tests failed')
  process.exit(1)
}

