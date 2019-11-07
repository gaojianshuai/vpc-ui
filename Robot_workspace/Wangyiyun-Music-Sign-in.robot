*** Settings ***
Library           Selenium2Library
Resource          common.txt

*** Test Cases ***
Sign_in_wangyiyun
    Open Browser    https://music.163.com/#    gc
    Set Window Size    1920    1080
    Maximize Browser Window
    Wait Until Page Contains    网易云音乐    5
    wait click element    css=a[data-action="login"]
    Wait Until Page Contains    微信登录    5
    wait click element    css=#j-official-terms
    wait click element    css=.u-mlg2-qq
    Select Window    title=QQ帐号安全登录
    Wait Until Page Contains    QQ登录    5
    sleep    3
    wait click element    xpath=//*[@id="switcher_plogin"]
    wait input element    css=#u    1170527913
    wait input element    css=#p    gjs19900704
    wait click element    css=#login_button
    Wait Until Page Contains    Justlive55    5
