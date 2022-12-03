$(document).ready(function () {
  let row_id = null;

  console.log("***Table***");
  const url = "api/mailings/";
  console.log(url);
  let table = $("#SP_Table").DataTable({
    ajax: {
      url: url,
      dataSrc: "",
    },
    columns: [
      { data: "id", visible: false },
      { data: "status" },
      { data: "start_date" },
      { data: "stop_date" },
      { data: "message" },
      { data: "phones" },
      { data: "clients", visible: false },
    ],
    DisplayLength: 10,
    processing: true,
    lengthMenu: [
      [10, 15, 20, -1],
      [10, 15, 20, "Все"],
    ],
    createdRow: function (row, data) {
      if (data.status) {
        $("td", row).eq(0).html("Ожидание");
      } else {
        $("td", row).eq(0).html("Завершена");
      }
    },
  });

  $("#SP_Table tbody").on("click", "tr", function () {
    if ($(this).hasClass("selected")) {
      $(this).removeClass("selected");
    } else {
      table.$("tr.selected").removeClass("selected");
      $(this).addClass("selected");
      var data = table.row(table.$("tr.selected")).data();
      console.table(data);
      row_id = data["id"];
    }
  });

  $("#StatTaskButton").on("click", function () {
    $("#input_all_mes").val("");
    $("#input_suc_mes").val("");
    $("#list_phones").empty();
    $("#list_phones").append(
      `<thead>
            <tr>
                <th scope="col">Телефон</th>
                <th scope="col">Статус</th>
            </tr>
        </thead>`
    );
    $.ajax({
      type: "GET",
      url: "api/messages/?mailing=" + row_id,
      success: function (response) {
        let suc_i = 0;
        for (i = 0; i < response.length; i++) {
          console.log(response[i].phone);
          $("#list_phones").append(
            `<tr><td>${response[i].phone}</td><td>${response[i].status}</td></tr>`
          );
          if (response[i].status == "send_success") {
            suc_i++;
          }
        }
        $("#input_all_mes").val(response.length);
        $("#input_suc_mes").val(suc_i);
      },
    });
    $("#StatTaskModal").fadeIn();
  });

  $("#StatTaskClose1").on("click", function () {
    $("#StatTaskModal").fadeOut();
  });

  $("#StatTaskClose2").on("click", function () {
    $("#StatTaskModal").fadeOut();
  });

  $("#CreateTaskButton").on("click", function () {
    create_edit_mode = "create";
    $("#edit-create-norm-title").html("Создание новой рассылки");
    $("#CreateTaskOkButton").html("Создать");
    $("#input_start_date").empty();
    $("#input_stop_date").empty();
    $("#input_text").val("");
    console.log("CREATE");
    $("#CreatEditTaskModal").fadeIn();
  });

  $("#CeateTaskClose1").on("click", function () {
    $("#CreatEditTaskModal").fadeOut();
  });

  $("#CeateTaskClose2").on("click", function () {
    $("#CreatEditTaskModal").fadeOut();
  });

  $("#CreateTaskOkButton").on("click", get_operator);

  function get_operator() {
    let add_to_URL = "?operator_code=";
    if ($("#op1").is(":checked")) {
      add_to_URL += "-Билайн";
    }
    if ($("#op2").is(":checked")) {
      add_to_URL += "-МТС";
    }
    if ($("#op3").is(":checked")) {
      add_to_URL += "-Мегафон";
    }

    $.ajax({
      type: "GET",
      url: "api/clients/" + add_to_URL,
      success: function (response) {
        console.log(JSON.stringify(response));
        get_tag(response);
      },
    });
  }

  function get_tag(mas_operator) {
    console.log(
      $("#tag1").is(":checked"),
      $("#tag2").is(":checked"),
      $("#tag3").is(":checked")
    );
    let add_to_URL = "?tag=";
    if ($("#tag1").is(":checked")) {
      add_to_URL += "-премиум";
    }
    if ($("#tag2").is(":checked")) {
      add_to_URL += "-эконом";
    }
    if ($("#tag3").is(":checked")) {
      add_to_URL += "-лайт";
    }

    $.ajax({
      type: "GET",
      url: "api/clients/" + add_to_URL,
      success: function (response) {
        console.log(JSON.stringify(response));
        let clients = [];
        for (i = 0; i < mas_operator.length; i++) {
          console.log("operator", mas_operator[i]);
          for (j = 0; j < response.length; j++) {
            console.log("status", response[j]);
            if (mas_operator[i].id == response[j].id) {
              clients.push(mas_operator[i].id);
              break;
            }
          }
        }
        console.log({ clients });
        console.log(typeof clients);
        create_task(clients);
      },
    });
  }

  function create_task(clients) {
    let new_task = {
      start_date: $("#input_start_date").val(),
      stop_date: $("#input_stop_date").val(),
      message: $("#input_text").val(),
      clients: clients,
    };
    csrftoken = window.CSRF_TOKEN;
    function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
    }
    $.ajaxSetup({
      beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      },
    });

    $.ajax({
      type: "POST",
      url: "api/mailings/",
      data: JSON.stringify(new_task),
      contentType: "application/json",
      dataType: "json",
      success: function (data) {
        console.log(JSON.stringify(data));
        table.ajax.reload();
        $("#CreatEditTaskModal").fadeOut();
      },
      error: function (errMsg) {
        alert(`Ошибка при создании рассылки\n${JSON.stringify(errMsg)}`);
        console.log(JSON.stringify(errMsg));
      },
    });
  }

  $("#DeleteTaskButton").on("click", function () {
    csrftoken = window.CSRF_TOKEN;
    function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
    }
    $.ajaxSetup({
      beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      },
    });

    $.ajax({
      type: "DELETE",
      url: "api/mailings/" + row_id + "/",
      contentType: "application/json",
      dataType: "json",
      success: function (data) {
        console.log(JSON.stringify(data));
        table.ajax.reload();
      },
      error: function (errMsg) {
        alert(`Ошибка при удалении задачи\n${JSON.stringify(errMsg)}`);
        console.log(JSON.stringify(errMsg));
      },
    });
  });
});
