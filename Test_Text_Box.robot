*** Settings ***
Library     SeleniumLibrary
Library    BuiltIn
Library    insert_data.InsertData
Library    verify_data.VerifyData
*** Keywords ***
Open Browser Page
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    
# Find Data
    # Find Name
    # Find Email
    # Find Current Address
    # Find Permanent Address
    
*** Variables ***
${url}    https://demoqa.com/text-box
&{dict_values}    Full Name=sdasdas    Email=razvan@yahoo.com    Current Address=sdasda    Permanent Address=sadsadsa
${browser}    chrome


*** Test Cases ***
Test_text_box
    Open Browser Page
    Retrieve Text Boxes
    Insert Data    ${dict_values}
    Execute Javascript    window.scroll(0,300)
    Click Element   id=submit
    Check Data
    Sleep    5
    Close Browser
    
    