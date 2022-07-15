var eeee;
var now_page = 0;
var SetMinute = 0;

//==================================
//副程式 : 新增textarea(Test Case、Mutant)
//==================================
function Add_CT() {
    //暫存新的Editor
    let newmyCodeMirror;
    //新增TEXTAREA
    let btn = document.createElement("TEXTAREA");
    //預設內容
    let btn_text = document.createTextNode("#CT...");
    // 現在CT數量
    let check_count = calculation_CT();

    //設定外部id
    btn.setAttribute("id", "CT_" + (check_count + 1));
    //設定外部name
    btn.setAttribute("name", "mutant" + (check_count + 1));
    //放入預設內容
    btn.appendChild(btn_text);

    //新增到畫面上
    document.getElementById("Area_of_CT").appendChild(btn);

    //建立Editor
    newmyCodeMirror = CodeMirror.fromTextArea(document.getElementById("CT_" + (check_count + 1)), {
        mode: "python",
        lineNumbers: true,
        foldGutter: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
        readOnly: true
    });
    //大小(W,H)
    newmyCodeMirror.setSize(400, 150);
}

//==================================
//副程式 : 顯示textarea(Test Case、Mutant)
//==================================
function show_CT(amount, context) {
    let i;
    document.getElementById("Mutant_Amount").innerText = "Mutant Amount: " + String(rand_mutant.length);
    for (i = 1; i <= amount; i++) {
        //暫存新的Editor
        let newmyCodeMirror;
        //新增TEXTAREA
        let btn = document.createElement("TEXTAREA");
        //預設內容
        let btn_text = document.createTextNode(context[i - 1]);
        // 現在CT數量
        let check_count = calculation_CT();

        //設定外部id
        btn.setAttribute("id", "CT_" + (check_count + 1));
        //設定外部name
        btn.setAttribute("name", "mutant" + (check_count + 1));
        //放入預設內容
        btn.appendChild(btn_text);

        //新增到畫面上
        document.getElementById("Area_of_CT").appendChild(btn);

        //建立Editor
        eeee = CodeMirror.fromTextArea(document.getElementById("CT_" + (check_count + 1)), {
            mode: "python",
            lineNumbers: true,
            foldGutter: true,
            gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
            readOnly: true
        });
        //大小(W,H)
        //newmyCodeMirror.setSize(400, 150);
    }

}

//==================================
//副程式 : 新增textarea(Editor)
//==================================
function Add_Editor() {
    temp = calculation_Editor();
    //暫存新的Editor
    let newmyCodeMirror;
    //新增TEXTAREA
    let btn = document.createElement("TEXTAREA");
    //預設內容
    //let btn_text;
    let btn_text = document.createTextNode("#Edtor..." + (temp + 1));

    //設定外部id
    btn.setAttribute("id", "code-python" + "-" + (temp + 1));
    //設定外部name
    btn.setAttribute("name", "code" + (temp + 1));
    //放入預設內容
    btn.appendChild(btn_text);

    //新增到畫面上
    document.getElementById("Area_of_Editor").appendChild(btn);

    //建立Editor
    newmyCodeMirror = CodeMirror.fromTextArea(document.getElementById("code-python" + "-" + (temp + 1)), {
        mode: "python",
        lineNumbers: true,
        foldGutter: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
        autocomplete: true
    });
    //大小(W,H)
    newmyCodeMirror.setSize(700, 150)
}

//==================================
//副程式 : 計算Editor數量
//==================================
function calculation_Editor() {
    let check_count = 0;
    while (document.getElementById("code-python-" + String(check_count + 1))) {
        check_count = check_count + 1;
        console.log("check_count", check_count);
    }
    return check_count
}

//==================================
//副程式 : 計算CT數量
//==================================
function calculation_CT() {
    let check_count = 0;
    while (document.getElementById("CT_" + String(check_count + 1))) {
        check_count = check_count + 1;
        console.log("check_count", check_count);
    }
    return check_count
}

//==================================
//副程式 : Initial Editor
//==================================
function Initial_Editor(te_python) {
    let myCodeMirror
    myCodeMirror = CodeMirror.fromTextArea(te_python, {
        mode: "python",
        lineNumbers: true,
        foldGutter: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"]
    });
    //大小(W,H)
    //myCodeMirror.setSize(900, 800)
}

//==================================
//副程式 : Initial Area_of_CT
//==================================
function Initial_CT(CT_count) {
    for (let i = 1; i <= CT_count; i++) {
        let CT_id = "CT_" + String(i);
        let temp_CT = document.getElementById(String(CT_id));
        let temp_codemirror

        temp_codemirror = CodeMirror.fromTextArea(temp_CT, {
            mode: "python",
            lineNumbers: true,
            foldGutter: true,
            gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
            //唯獨模式
            readOnly: true
        });
        //大小(W,H)
        //temp_codemirror.setSize(400, 150)
    }
}

//==================================
//副程式 : Initial Editor(Attacker)
//==================================
function Initial_Editor_Attacker(te_python) {
    let myCodeMirror
    myCodeMirror = CodeMirror.fromTextArea(te_python, {
        mode: "python",
        lineNumbers: true,
        foldGutter: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
        autocomplete: true
    });
    //大小(W,H)
    myCodeMirror.setSize(700, 150)
}

//==================================
//副程式 : Initial Area_of_CT(Attacker)
//==================================
function Initial_CT_Attacker(CT_count) {
    for (let i = 1; i <= CT_count; i++) {
        let CT_id = "CT_" + String(i);
        let temp_CT = document.getElementById(String(CT_id));
        let temp_codemirror

        temp_codemirror = CodeMirror.fromTextArea(temp_CT, {
            mode: "python",
            lineNumbers: true,
            foldGutter: true,
            gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
            //唯獨模式
            readOnly: true
        });
        //大小(W,H)
        temp_codemirror.setSize(700, 800)
    }
}

//
function same_page_previous(content) {
    if (now_page - 1 <= 0) {
        now_page = (content.length) - 1;
        eeee.setValue(content[now_page])

    } else {
        now_page = now_page - 1
        eeee.setValue(content[now_page])
    }

}

//
function same_page_next(content) {
    if (now_page + 1 >= content.length) {
        now_page = 0
        eeee.setValue(content[now_page])
    } else {
        now_page = now_page + 1
        eeee.setValue(content[now_page])
    }
}


//
function overlay_on() {
    document.getElementById("overlay").style.display = "inline";
}

function overlay_off() {
    document.getElementById("overlay").style.display = "none";
}


//Dialog Show
function showsubmitdialog(dialog) {
    document.getElementById(String(dialog)).showModal();
}

//Dialog Hide
function hidesubmitdialog(dialog) {
    document.getElementById(String(dialog)).close();
}


//Timer
function timer() {
    SetMinute += 1;
    var Check_i = document.getElementById("Check_i");

    var Cal_Hour = Math.floor(SetMinute / 3600);
    var Cal_Minute = Math.floor(Math.floor(SetMinute % 3600) / 60);
    var Cal_Second = SetMinute % 60;

    Check_i.innerHTML = Cal_Hour + ":" + Cal_Minute + ":" + Cal_Second + "";
}
