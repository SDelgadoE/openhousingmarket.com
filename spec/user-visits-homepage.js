const chai = require('chai')
const chaiHttp = require('chai-http')
const expect = chai.expect
chai.use(chaiHttp)

const app = require('../src/app')

describe('When the user visits the homepage', () => {

  it('Show a heading with the company name', () =>

    chai.request(app).get('/').then(res => {

      expect(res).to.have.status(200)
      expect(res).to.be.html
      expect(res.text).to.match(/<h1[^>]*>Open Housing Market<\/h1>/)

    }).catch(err => { throw err })

  )

})
