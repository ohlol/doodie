$(function() {
    var Status = function(type) {
        var self = this;

        self.label = type.charAt(0).toUpperCase() + type.slice(1);
        self.value = ko.observable();
    };

    var QuickViewModel = function() {
        var self = this;

        self.statuses = ko.observableArray([
            {
                id: "acknowledged",
                status: new Status("acknowledged")
            },
            {
                id: "triggered",
                status: new Status("triggered")
            }
        ]);
    };

    qvm = new QuickViewModel();
    ko.applyBindings(qvm);
});

function getIncidents() {
    $.getJSON("/incidents/count/acknowledged,triggered", function(data) {
        if (data.hasOwnProperty("message")) {
            for (var i = 0; i < data.message.length; i++) {
                for (var j = 0; j < qvm.statuses().length; j++) {
                    if (qvm.statuses()[j].id === data.message[i].id) {
                        qvm.statuses()[j].status.value(data.message[i].value);
                    }
                }
            }
        }
    }).error(function() {
        for (var i = 0; i < qvm.statuses().length; i++) {
            qvm.status()[i].status().value("unknown");
        }
    });

    setTimeout(getIncidents, 100000);
}
