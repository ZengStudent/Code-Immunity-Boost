var editor_cm;
var originalcode_cm;
var opposite_cm;
var opposite_ma;
var now_page = 0;

function aggression_show_originalcode(context) {
     //新增textarea
    let btn = document.createElement("TEXTAREA");
    //預設內容
    let btn_text = document.createTextNode(context);

    //設定外部id
    btn.setAttribute("id", "originalcode_cm");
    //設定外部name
    btn.setAttribute("name", "oricode1");
    //放入預設內容
    btn.appendChild(btn_text);

    //新增到畫面上
    document.getElementById("area_of_originalcode").appendChild(btn);

    //建立Editor
    originalcode_cm = CodeMirror.fromTextArea(document.getElementById("originalcode_cm"), {
        mode: "python",
        lineNumbers: true,
        foldGutter: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
        readOnly: true
    });
}


//==================================
//副程式 : 顯示textarea(Test Case、Mutant)
//==================================
function aggression_show_CT(amount, context) {

    opposite_ma = document.getElementById("Mutant_Amount");
    opposite_ma.innerHTML = "1 - " + String(context.length);

    //新增textarea
    let btn = document.createElement("TEXTAREA");
    //預設內容
    let btn_text = document.createTextNode(context[0]);

    //設定外部id
    btn.setAttribute("id", "opposites_cm");
    //設定外部name
    btn.setAttribute("name", "mutant1");
    //放入預設內容
    btn.appendChild(btn_text);

    //新增到畫面上
    document.getElementById("area_of_opposites").appendChild(btn);

    //建立Editor
    opposite_cm = CodeMirror.fromTextArea(document.getElementById("opposites_cm"), {
        mode: "python",
        lineNumbers: true,
        foldGutter: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
        readOnly: true
    });

}

//==================================
//副程式 : Initial Editor
//==================================
function aggression_Initial_Editor(editor_textarea) {
    editor_cm = CodeMirror.fromTextArea(editor_textarea, {
        mode: "python",
        lineNumbers: true,
        foldGutter: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"]
    });

}


function aggression_default(code) {
    editor_cm.setValue(code)
}

function aggression_rewrite(code) {
    editor_cm.setValue(code)
}

//
function aggression_opposite_editor_previous(content) {
    if (now_page - 1 <= 0) {
        now_page = (content.length) - 1;
        opposite_cm.setValue(content[now_page])

    } else {
        now_page = now_page - 1
        opposite_cm.setValue(content[now_page])
    }

    //
    opposite_ma = document.getElementById("Mutant_Amount");
    opposite_ma.innerHTML = String(now_page + 1) + " - " + String(content.length);
}

//
function aggression_opposite_editor_next(content) {
    if (now_page + 1 >= content.length) {
        now_page = 0
        opposite_cm.setValue(content[now_page])
    } else {
        now_page = now_page + 1
        opposite_cm.setValue(content[now_page])
    }
    //
   opposite_ma = document.getElementById("Mutant_Amount");
   opposite_ma.innerHTML = String(now_page + 1) + " - " + String(content.length);
}