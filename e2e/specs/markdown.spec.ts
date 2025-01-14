/**
 * @license
 * Copyright 2018-2019 Streamlit Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/// <reference types="cypress" />

describe("st.markdown", () => {
  before(() => {
    cy.visit("http://localhost:3000/");
  });

  it("displays a markdown", () => {
    cy.get(".element-container").should("have.length", 2);

    cy.get(".element-container .stText p")
      .first()
      .contains("This markdown is awesome!");

    cy.get(".element-container .stText p")
      .last()
      .contains("This html in <div>markdown</div> is escaped!");
  });
});
