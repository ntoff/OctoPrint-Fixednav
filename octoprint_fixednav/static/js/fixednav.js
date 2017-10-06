/*
 * View model for OctoPrint-Fixednav
 *
 * Author: ntoff
 * License: AGPLv3
 */
$(function() {
    function FixednavViewModel(parameters) {
        var self = this;

        if ($("#touch body").length ==0 ) {
            $("div.page-container > #navbar").eq(0).removeClass("navbar-static-top").addClass("navbar-fixed-top");
            $("body").css({ "padding-top": "40px" })
        }
    }

    OCTOPRINT_VIEWMODELS.push([
        FixednavViewModel
    ]);
});
