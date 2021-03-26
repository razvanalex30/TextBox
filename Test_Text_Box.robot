*** Settings ***
Library     SeleniumLibrary
Library    BuiltIn
Library    insert_data.InsertData
Library    verify_data.VerifyData
*** Keywords ***
Open Browser Page
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    
Insert Data
    Insert Full Name    ${full_name}
    Insert Email    ${email}
    Insert Current Address    ${current_address}
    Insert Permanent Address    ${permanent_address}

Find Data
    Find Name
    Find Email
    Find Current Address
    Find Permanent Address
    
*** Variables ***
${url}    https://demoqa.com/text-box
${browser}    chrome
${full_name}    sdsadsa
${email}    asdsada@yahoo.com
${current_address}    sdasdsadsa
${permanent_address}    sadsadsadsasdasdsa


*** Test Cases ***
Test_text_box
    Open Browser Page
    Insert Data
    Execute Javascript    window.scroll(0,300)
    Click Element   id=submit
    Find Data
    Sleep    5
    Close Browser
    
    