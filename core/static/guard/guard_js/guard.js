//Editor的CodeMirror
var editor_cm;
//Editor內容
var editor_cm_many = new Array(40);
//Original Code的CodeMirror
var originalcode_cm;
//Opposites的CodeMirror
var opposite_cm;
//Opposites的頁數
var opposite_ma;
//現在Opposites的頁數
var now_page = 0;
//現在Editor的頁數
var now_breadpage = 1;
//Editor上限
var breadpagemax = 40;


//==================================
//副程式 : 顯示textarea(Original Code)
//==================================
function guard_show_originalcode(context) {
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
function guard_show_CT(amount, context) {

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
function guard_Initial_Editor(editor_textarea) {
    editor_cm = CodeMirror.fromTextArea(editor_textarea, {
        mode: "python",
        lineNumbers: true,
        foldGutter: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
    });

    for (let i = 1; i < breadpagemax; i++) {
        editor_cm_many[i] = "editor_cm_" + String(i + 1);
    }

    //現在Editor數量內容
    let EditorAcount = document.getElementById("Editor_Acount");
    //設定現在Editor數量內容
    EditorAcount.value = 1;

    //Editor Decrease Button
    let editordecreasebutton = document.getElementById("editordecrease");
    editordecreasebutton.disabled = true;

    //
    let breadbutton_1 = document.getElementById("breadbutton_1");
    breadbutton_1.disabled = true;


}

//==================================
//副程式 : Editor恢復預設內容
//==================================
function guard_default(code) {

    editor_cm.setValue(code);
    editor_cm_many[0] = code;

    //
    let breadhiddeninput_1 = document.getElementById("breadhiddeninput_1");
    breadhiddeninput_1.value = code;
}

//==================================
//副程式 : Editor 覆蓋內容
//==================================
function guard_rewrite(code) {
    editor_cm.setValue(code)
}

//==================================
//副程式 : Opposites 顯示上一頁內容
//==================================
function guard_opposite_editor_previous(content) {
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

//==================================
//副程式 : Opposites 顯示下一頁內容
//==================================
function guard_opposite_editor_next(content) {
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

//==================================
//副程式 : 新增Editor
//==================================
function guard_editor_increase() {
    //Editor Bread
    let bread = document.getElementById("breadeditor");
    //Editor Increase Button
    let editorincreasebutton = document.getElementById("editorincrease");
    //Editor Decrease Button
    let editordecreasebutton = document.getElementById("editordecrease");

    //如果Editor的數量未達上限
    if (bread.childElementCount < breadpagemax) {
        //現在Editor數量
        let breadcount = bread.childElementCount + 1
        //新增Editor頁面按鈕
        let breadbutton = document.createElement("button")
        //新增Editor Bread Child
        let breadli = document.createElement("li")
        //
        let breadhiddeninput = document.createElement("textarea");

        //設定Editor Bread Child的id
        breadli.setAttribute("id", "breadli_" + String(breadcount));
        //設定Editor Bread Child的外觀
        breadli.setAttribute("class", "breadcrumb-item");

        //Editor頁面按鈕的id
        breadbutton.setAttribute("id", "breadbutton_" + String(breadcount));
        //Editor頁面按鈕的外觀
        breadbutton.setAttribute("class", "btn btn-primary btn-simple btn-fab btn-icon btn-round");
        //Editor頁面按鈕的功能
        breadbutton.onclick = function () {
            breadbutton_update(breadcount);
        }
        ////Editor頁面按鈕的內容文字
        breadbutton.innerText = breadcount;

        //
        let hiddendiv = document.getElementById("hiddendiv");
        //
        breadhiddeninput.setAttribute("id", "breadhiddeninput_" + String(breadcount));
        //
        breadhiddeninput.setAttribute("name", "breadhiddeninput_" + String(breadcount));
        //
        //breadhiddeninput.setAttribute("style","display:none;");
        //
        breadhiddeninput.value = " ";
        //
        hiddendiv.appendChild(breadhiddeninput);


        //Editor Bread Child新增子元件
        breadli.appendChild(breadbutton);
        //Editor Bread新增子元件
        bread.appendChild(breadli);

        //現在Editor數量內容
        let EditorAcount = document.getElementById("Editor_Acount");
        //設定現在Editor數量內容
        EditorAcount.value = bread.childElementCount;

        //如果有2個以上的Editor，Editor Decrease Button設為可用
        editordecreasebutton.disabled = false;

        //如果達上限，Editor Increase Button設為Disabled
        if (breadcount === breadpagemax) {
            editorincreasebutton.disabled = true;
        }
    }
    //如果Editor的數量已達上限
    else {
        alert("最大 40 個Editor");
    }

}


//==================================
//副程式 : 刪除Editor
//刪除當前顯示頁數的Editor
//==================================
function guard_editor_decrease() {
    //Editor Increase Button
    let editorincreasebutton = document.getElementById("editorincrease");
    //Editor Decrease Button
    let editordecreasebutton = document.getElementById("editordecrease");
    //
    let hiddendiv = document.getElementById("hiddendiv");
    //Editor Bread
    let bread = document.getElementById("breadeditor");
    //現在Editor數量內容
    let EditorAcount = document.getElementById("Editor_Acount");


    //刪除第一個
    if (now_breadpage === 1) {
        //只有兩個Editor
        if (bread.childElementCount === 2) {
            //要刪除的textarea
            let breadhiddeninput = document.getElementById("breadhiddeninput_1");
            //移除
            breadhiddeninput.parentNode.removeChild(breadhiddeninput);
            //第二個textarea
            breadhiddeninput = document.getElementById("breadhiddeninput_2");
            //將第二個textarea改為第一個
            breadhiddeninput.setAttribute("id", "breadhiddeninput_1");
            //將第二個textarea改為第一個
            breadhiddeninput.setAttribute("name", "breadhiddeninput_1");

            //要刪除的頁數清單
            let breadli = document.getElementById("breadli_1");
            //移除，同時刪除子節點Button
            breadli.parentNode.removeChild(breadli);
            //第二個頁數清單(li)
            breadli = document.getElementById("breadli_2");
            //將第二個頁數清單(li)改為第一個
            breadli.setAttribute("id", "breadli_1");
            //將第二個t頁數清單(li)改為第一個
            breadli.setAttribute("name", "breadli_1");

            //第二個頁數Button
            let breadbutton = document.getElementById("breadbutton_2");
            //第二個頁數Button改為第一個
            breadbutton.setAttribute("id", "breadbutton_1");
            //第二個頁數Button的功能改為更新第1個
            breadbutton.onclick = function () {
                breadbutton_update(1)
            };
            //第二個頁數Button的內容文字
            breadbutton.innerText = 1;

            //將第1個Editor內容，改變為第2個Editor內容
            editor_cm_many[0] = editor_cm_many[1];
            //第2個Editor內容，改變為預設值
            editor_cm_many[1] = "editor_cm_2";
            //現在Editor的頁數改為第一頁
            now_breadpage = 1;

            //Editor 覆蓋內容，改變為第1個Editor內容
            guard_rewrite(editor_cm_many[0]);
            //
            document.getElementById("breadbutton_1").disabled = true;

            alert("刪除(刪除第一個、只有兩個Editor)!!!!");
        }
        //3(含)個Editor以上
        else {
            //要刪除的textarea
            let breadhiddeninput = document.getElementById("breadhiddeninput_1");
            //移除
            breadhiddeninput.parentNode.removeChild(breadhiddeninput);
            //後面的textarea
            for (let i = 2; i <= bread.childElementCount; i++) {
                //從第二個textarea開始
                breadhiddeninput = document.getElementById("breadhiddeninput_" + String(i));
                //改為前一個
                breadhiddeninput.setAttribute("id", "breadhiddeninput_" + String(i - 1));
                //改為前一個
                breadhiddeninput.setAttribute("name", "breadhiddeninput_" + String(i - 1));
            }


            //要刪除的頁數清單
            let breadli = document.getElementById("breadli_1");
            //移除，同時刪除子節點Button
            breadli.parentNode.removeChild(breadli);

            //後面的頁數清單(li)
            //因為前面刪除了li，所以childElementCount數量會減1
            for (let i = 1; i <= bread.childElementCount; i++) {
                //從第二個頁數清單(li)開始
                breadli = document.getElementById("breadli_" + String(i + 1));
                //改為前一個
                breadli.setAttribute("id", "breadli_" + String(i));
                //改為前一個
                breadli.setAttribute("name", "breadli_" + String(i));
            }

            for (let i = 1; i <= bread.childElementCount; i++) {
                //從第二個頁數Button開始
                let breadbutton = document.getElementById("breadbutton_" + String(i + 1));
                //頁數Button改為前一個
                breadbutton.setAttribute("id", "breadbutton_" + String(i));
                //頁數Button的功能改為前一個
                breadbutton.onclick = function () {
                    breadbutton_update(i);
                }


                //頁數Button的內容文字改為前一個
                breadbutton.innerText = i;
            }

            //Editor內容
            for (let i = 1; i <= bread.childElementCount; i++) {
                //將Editor內容開始向前移動
                editor_cm_many[i - 1] = editor_cm_many[i];

                //如果到達最後一個Editor
                if (i === bread.childElementCount) {
                    //最後一個Editor改為預設值
                    editor_cm_many[i] = "editor_cm_" + String(i);
                }
            }

            //現在Editor的頁數改為第一頁
            now_breadpage = 1;
            //Editor 覆蓋內容，改變為第1個Editor內容
            guard_rewrite(editor_cm_many[0]);
            //將第1個頁數Button設為不可用
            document.getElementById("breadbutton_1").disabled = true;

            alert("刪除(刪除第一個、3(含)個Editor以上)!!!!");
        }
    }
    //刪除最後一個
    else if (now_breadpage === bread.childElementCount) {

        //要刪除的textarea
        let breadhiddeninput = document.getElementById("breadhiddeninput_" + String(bread.childElementCount));
        //移除
        breadhiddeninput.parentNode.removeChild(breadhiddeninput);

        //要刪除的頁數清單
        let breadli = document.getElementById("breadli_" + String(bread.childElementCount));
        //移除，同時刪除子節點Button
        breadli.parentNode.removeChild(breadli);

        //現在Editor的頁數改為現在Editor的頁數的前一頁
        now_breadpage = now_breadpage - 1;
        //Editor覆蓋內容，改變為前1個Editor內容
        guard_rewrite(editor_cm_many[now_breadpage - 1]);
        //將現在的頁數Button設為不可用
        document.getElementById("breadbutton_" + String(now_breadpage)).disabled = true;

        alert("最後一個");
    }
    //刪除中間
    else {
        //要刪除的textarea
        let breadhiddeninput = document.getElementById("breadhiddeninput_" + String(now_breadpage));
        //移除
        breadhiddeninput.parentNode.removeChild(breadhiddeninput);
        //後面的textarea
        for (let i = now_breadpage + 1; i <= bread.childElementCount; i++) {
            //從刪除的textarea後面一個開始
            breadhiddeninput = document.getElementById("breadhiddeninput_" + String(i));
            //改為前一個
            breadhiddeninput.setAttribute("id", "breadhiddeninput_" + String(i - 1));
            //改為前一個
            breadhiddeninput.setAttribute("name", "breadhiddeninput_" + String(i - 1));
        }


        //要刪除的頁數清單
        let breadli = document.getElementById("breadli_" + String(now_breadpage));
        //移除，同時刪除子節點Button
        breadli.parentNode.removeChild(breadli);

        //後面的頁數清單(li)
        //因為前面刪除了li，所以childElementCount數量會減1
        for (let i = now_breadpage; i < bread.childElementCount + 1; i++) {
            //從要刪除的頁數清單(li)後面一個開始
            breadli = document.getElementById("breadli_" + String(i + 1));
            //改為前一個
            breadli.setAttribute("id", "breadli_" + String(i));
            //改為前一個
            breadli.setAttribute("name", "breadli_" + String(i));
        }

        for (let i = now_breadpage; i < bread.childElementCount + 1; i++) {
            //從要刪除的頁數Button後面一個開始
            let breadbutton = document.getElementById("breadbutton_" + String(i + 1));
            //頁數Button改為前一個
            breadbutton.setAttribute("id", "breadbutton_" + String(i));
            //頁數Button的功能改為前一個
            breadbutton.onclick = function () {
                breadbutton_update(i)
            };
            //頁數Button的內容文字改為前一個
            breadbutton.innerText = i;
        }


        //Editor內容
        for (let i = now_breadpage; i < bread.childElementCount + 1; i++) {
            //將Editor內容開始向前移動
            editor_cm_many[i - 1] = editor_cm_many[i];

            //如果到達最後一個Editor
            if (i === bread.childElementCount) {
                //最後一個Editor改為預設值
                editor_cm_many[i] = "editor_cm_" + String(i);
            }
        }

        //現在Editor的頁數改為前一頁
        now_breadpage = now_breadpage - 1;
        //Editor 覆蓋內容，改變為第1個Editor內容
        guard_rewrite(editor_cm_many[now_breadpage - 1]);
        //將現在的頁數Button設為不可用
        document.getElementById("breadbutton_" + String(now_breadpage)).disabled = true;

        alert("中間");
    }

    //設定現在Editor數量內容
    EditorAcount.value = bread.childElementCount;
    //如果Editor的數量有2(含)個以上，則啟用editordecreasebutton
    if(bread.childElementCount > 1) editordecreasebutton.disabled = false;
    //如果Editor的數量是1個，則禁用editordecreasebutton
    else editordecreasebutton.disabled = true;
    //如果Editor的數量少於最大數量，則啟用editorincreasebutton
    if(bread.childElementCount <= breadpagemax) editorincreasebutton.disabled = false;
    //如果Editor的數量是最大數量，則禁用editorincreasebutton
    else editorincreasebutton.disabled = true;
}


//==================================
//副程式 : Save Editor
//==================================
function guard_editor_save() {
    //依照現在Editor頁數，儲存內容(前端)
    editor_cm_many[now_breadpage - 1] = editor_cm.getValue();

    //依照現在Editor頁數，儲存內容(後端)
    document.getElementById("breadhiddeninput_" + String(now_breadpage)).value = editor_cm.getValue();
}

//==================================
//副程式 : breadbutton
//==================================
function breadbutton_update(breadbuttonid) {

    //當前Editor頁數
    let old_breadbutton = document.getElementById("breadbutton_" + String(now_breadpage));
    //設為可使用
    old_breadbutton.disabled = false;
    //儲存內容
    guard_editor_save();

    //要切換的Editor頁數
    let new_breadbutton = document.getElementById("breadbutton_" + String(breadbuttonid));
    //設為不可使用
    new_breadbutton.disabled = true;

    //設定現在Editor頁數
    now_breadpage = breadbuttonid;

    //更新內容為，現在Editor頁數的內容
    guard_rewrite(editor_cm_many[now_breadpage - 1]);

    return null;
}


