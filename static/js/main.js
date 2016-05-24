var find_points_on_line = function (x1, y1, x2, y2) {
    var slope = Math.floor((y2 - y1) / (x2 - x1));
    var intercept = Math.floor(y1 - slope * x1);
    var points = [];
    for (var i = x1; i <= x2; i++) {
        var y = slope * i + intercept;
        points.push(Math.floor(y));
    }
    return points;
};


var find_points_on_lines = function (lines) {
    /**
     * An array of arrays;
     * Input
     * [
     *  [x1, y1, x2, y2]
     * ]
     *
     */

    var points = [];
    for (var i = 0; i < lines.length; i++) {
        var line = lines[i];
        var x1 = line[0],
            y1 = line[1],
            x2 = line[2],
            y2 = line[3];
        points = points.concat(find_points_on_line(x1, y1, x2, y2))
    }
    return points;
};
var default_scenario = {
    'living_status': 'live_away',
    'institution': 'UW',
    'family_size': 4,
    'hours_worked': 500,
    'interest_earned': 4
};

var validateFormElement = function (formElement) {
    var min = parseFloat(formElement.attr('min'));
    var max = parseFloat(formElement.attr('max'));
    var val = parseFloat(formElement.val());
    return val >= min && val <= max;

};

var markError = function (formElement) {
    formElement.parent().addClass('has-error');
};

var unmarkError = function (formElement) {
    formElement.parent().removeClass('has-error');
};

var build_scenario = function (arguments, modifiers) {
    var scenario = {};
    var invalidFormData = false;
    for (var i = 0; i < arguments.length; i++) {
        var arg = arguments[i];
        var formElement = jQuery("#" + arg);

        if (formElement.hasClass('validate')) {
            if (!validateFormElement(formElement)) {
                markError(formElement);
                invalidFormData = true;
            } else {
                unmarkError(formElement);
            }
        }

        var val = formElement.val();
        if (val === undefined) {
            val = default_scenario[arg];
        }
        if (modifiers !== undefined && modifiers[arg] !== undefined) {
            scenario[arg] = modifiers[arg](val);
        } else {
            scenario[arg] = val;
        }
    }
    if (invalidFormData) {
        throw "Form data is invalid";
    } else {
        return scenario;
    }
};

var make_scenario = function (arguments) {
    /**
     * :param:arguments Object containing keyword arguments for scenario
     *          - calendar_year
     *          - state
     *          - percent_discretionary_income_saved
     *          - years_of_college_saving
     *          - discretionary_income_contribution
     *          - cost_of_attendance_lower @deprecated
     *          - cost_of_attendance_upper @deprecated
     */
    return arguments;

};