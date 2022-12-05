describe('happy path', () => {
  it('eth address', () => {
    cy.visit('/')
    cy.get('div[data-testid=dropdown-token]').click()
    cy.get('div.item:nth-child(1)').click()
    cy.get('div[data-testid=input-address] input').type(Cypress.env('eth_address'))
    cy.get('button[data-testid=button-find]').click()
    cy.get('h2[data-testid=header-value]').should("have.text", `${Cypress.env('eth_value')} ETH`)
  })
  it('usdc address', () => {
    cy.visit('/')
    cy.get('div[data-testid=dropdown-token]').click()
    cy.get('div.item:nth-child(2)').click()
    cy.get('div[data-testid=input-address] input').type(Cypress.env('usdc_address'))
    cy.get('button[data-testid=button-find]').click()
    cy.get('h2[data-testid=header-value]').should("have.text", `${Cypress.env('usdc_value')} USDC`)
  })
})