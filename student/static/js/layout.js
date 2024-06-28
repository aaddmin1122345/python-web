// 验证码刷新
function change_img(){
     document.getElementById("image_code").src = "/img/code/?time=" + Math.random();
}


// 发送邮箱验证码
function abcemail(){
    var username = $("input[id='id_username']").val();
    if (username == ""){
        alert("请输入用户名！");
        $("input[id='id_username']").focus();
    }
    //拿到参数后使用Ajax向后提交
    $.ajax({
        url:"/email/",  // 请求的地址
        type:"post",    // 请求的方式,使用method()也可以
        data:{
            "username":username,
            csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val(),
        },   //指定要提交给后端的数据
        success: function (res){ // 接收后端返回的结果
            // 后端返回的数据都放在res里面
            var m = res.msg
            if (m == 100){
                alert("验证码发送成功！");
            }else{
                alert("验证码发送失败！");
            }
        }
    })
}

function to_pwd(){
    var pwd = $("input[id='id_password']").val();
    var con_pwd = $("input[id='id_con_password']").val();
    if ( pwd != con_pwd){
        alert("两次密码不一致！");
        $("input[id='id_password']").focus();
    }
}

// 时间添加
var date = {
        format: 'yyyy-mm-dd',
        endDate: new Date,
        language: "zh-CN",
        autoclose: true
}
$('#id_student_time').datepicker(date);
$('#id_teacher_time').datepicker(date);


function page_input(){
    var pa = $("input[id='page_input']").val();
    console.log(pa)
    if (pa == "0"){
        alert("请重新输入！");
        $("input[id='page_input']").focus();
    }else{
        alert("!!!！");
    }
}