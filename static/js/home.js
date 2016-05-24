/**
 * Created by gautam on 10/26/15.
 * TODO: Solve SetTimeout need in Institutional aid switching based on SNG.
 */
jQuery(function () {
    var grouping = [
        'state_appropriation',
        'college_savings',
        'family_income',
        'pell_grant',
        'state_need_grant',
        'institutional_aid',
        'student_work',
        'affordable_debt',
        'additional_debt'
    ];

    var SCENARIO = {
        'state_appropriation': 1000
    };

    var yAxisTickFormat = function (tickValue) {
        var state_appr = SCENARIO['state_appropriation'];
        var y = parseInt(tickValue);
        if (y < state_appr) {
            return '';
        } else {
            return '';
        }

    };
    var update_ui_scenario = function (data) {
        var scenario = data['scenario'];
        var time_to_graduate = scenario['time_to_graduate'];
        var coa = data['plots']['cost_of_attendance'];
        var annual_coa;
        var total_coa;

        annual_coa = coa['tuition'] + coa['non_tuition'];
        total_coa = Math.floor(annual_coa * time_to_graduate);
        var ui_mfi = scenario['median_family_income'][0]['income'];
        $("#ui_mfi").val(accounting.formatNumber(ui_mfi, 0));
        $("#ui_total_coa").text(accounting.formatMoney(total_coa, '$', 0));

        jQuery('.scenario_val').each(function (i, obj) {
            var scenario_key = jQuery(obj).data('scenario');
            var element = jQuery(obj);
            var value = scenario[scenario_key];
            if (element.hasClass('currency-format')) {
                value = accounting.formatNumber(value, 0)
            }
            if (element.is('input')) {
                element.val(value);
            } else {
                element.text(value)
            }

        });

    };
    var chart_options = {
        bindto: "#chart",
        transition: 100,
        size: {
            height: 300,
            width: 1450

        },
        tooltip: {
            show: false
        },
        data: {
            rows: [],
            order: null,
            types: {
                college_savings: 'area',
                family_income: 'area',
                state_need_grant: 'area',
                pell_grant: 'area',
                'student_work': 'area',
                'state_appropriation': 'area',
                'institutional_aid': 'area',
                'affordable_debt': 'area',
                'additional_debt': 'area'
                // 'line', 'spline', 'step', 'area', 'area-step' are also available to stack
            },
            groups: [grouping],
            colors: {
                "college_savings": "#77933c",
                "family_income": "#c3d69b",
                "institutional_aid": "#95b3d7",
                "pell_grant": "#376092",
                "student_work": "#c77609",
                'state_appropriation': "#000000",
                'affordable_debt': "#E37676",
                'additional_debt': 'red'
            },
            names: {
                'college_savings': 'College savings',
                'family_income': 'Family contribution',
                'state_need_grant': 'State need grant',
                'pell_grant': 'Pell grant',
                'student_work': 'Student work',
                'state_appropriation': 'State appropriation',
                'institutional_aid': 'Institutional aid',
                'affordable_debt': 'Affordable debt',
                'additional_debt': 'Additional debt'
            }
        },
        axis: {
            y: {
                label: {
                    text: '$ / yr',
                    position: 'outer-middle'
                },
                show: true,
                tick: {
                    'format': yAxisTickFormat,
                    count: 1

                }
            },
            x: {
                min: 0,
                max: 200,
                tick: {
                    format: function (x) {
                        return x + '%';
                    },
                    values: [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
                },
                label: {
                    text: 'Percent median family income',
                    position: 'outer-center'
                }
            }
        },
        regions: [
            {
                'axis': 'x',
                'start': 1,
                'end': 198,
                'class': 'regionY'
            }
        ],
        legend: {
            item: {
                onmouseover: function (id) {
                    if (['state_appropriation', 'additional_debt'].indexOf(id) === -1) {
                        // Equivalent to `id not in ['state_appropriation', 'additional_debt']`
                        chart.focus(id);
                    } else {
                        chart.focus();
                    }
                },
                onclick: function (id) {
                    if (['state_appropriation', 'additional_debt'].indexOf(id) === -1) {
                        // Equivalent to `id not in ['state_appropriation', 'additional_debt']`
                        chart.toggle(id);
                    }
                    if (id === "state_need_grant" && !INSTITUTIONAL_AID_ALWAYS_USE_WEIGHTED_AVG) {
                        var $state_need_grant_shown = jQuery("#state_need_grant_shown");
                        var state_need_grant_shown = ($state_need_grant_shown.val() === "true");
                        $state_need_grant_shown.val((!state_need_grant_shown).toString());
                        setTimeout(change_value, 400);
                    }

                }
            }
        },

        point: {
            show: false
        }

    };
    var chart = c3.generate(chart_options);

    var expand_lines = function (plot) {
        var lines = plot['data'];
        return find_points_on_lines(lines);
    };

    var process_server_data = function (server_data) {
        var plots = server_data['plots'];
        var processed_plots = {};
        for (var i in plots) {
            if (!plots.hasOwnProperty(i)) continue;
            var plot = plots[i];
            var type = plot['type'];
            switch (type) {
                case 'line':
                    processed_plots[i] = expand_lines(plot);
                    break;
                case 'points':
                    processed_plots[i] = plot['data'];
                    break;
            }
        }
        return processed_plots;
    };


    function ui_bindings(scenario) {
        jQuery('.bound').each(function (i, obj) {
            var jQObj = jQuery(obj);
            var scenario_key = jQObj.data('scenario');

            if (jQObj.attr('type') === "checkbox") {
                scenario[scenario_key] = jQuery(obj).is(':checked');
            } else {
                var data_type = jQObj.data('type');
                var value = jQuery(obj).val();
                switch (data_type) {
                    case "boolean":
                        scenario[scenario_key] = value.toLowerCase() === "true";
                        break;
                    default:
                        scenario[scenario_key] = value;
                }


            }
        });
    }


    var change_value = function () {
        try {
            var scenario = build_scenario([
                'calendar_year',
                'state',
                'years_of_savings',
                'percent_discretionary_income_saved',
                'discretionary_income_contribution',
                'institution_type',
                'hours_worked',
                'interest_earned',
                'living_status',
                'institution',
                'family_size',
                'family_income_exclusion_threshold',
                'policy_change_tuition_adjustment'
            ], {
                'calendar_year': parseInt,
                'percent_saving': parseInt,
                'years_of_saving': parseInt,
                'contribution_percent': parseFloat,
                'interest_earned': parseFloat,
                'years_of_savings': parseFloat
            });
            ui_bindings(scenario);
        } catch (error) {
            console.log(error);
            return false;
        }


        function generate_additional_debt_graph(yaxis_max, json) {
            var additional_debt_plot = [];
            for (var i = 0; i < 200; i++) {
                additional_debt_plot.push(yaxis_max);
            }
            json['additional_debt'] = additional_debt_plot;
        }

        var POST_DATA = {
            'scenario': JSON.stringify(scenario),
            'plots': JSON.stringify(grouping.concat(['cost_of_attendance'])),
            'csrfmiddlewaretoken': CSRF_TOKEN

        };

        jQuery.post(URL_API_PLOT, POST_DATA, function (data) {
            var cost_of_attendance = data['plots']['cost_of_attendance'];
            var tuition = cost_of_attendance['tuition'];
            var non_tuition = cost_of_attendance['non_tuition'];
            var state_appr = data['plots']['state_appropriation']['data'][0];
            var yaxis_max = tuition + non_tuition + state_appr;
            var tuition_line_value = tuition + state_appr;
            SCENARIO = data['scenario'];
            chart.ygrids([{
                'text': 'Annual tuition $' + tuition,
                'position': 'middle',
                'class': 'tuition-line',
                'value': tuition_line_value
            }]);
            update_ui_scenario(data);
            delete data['plots']['cost_of_attendance'];
            var json = process_server_data(data);
            generate_additional_debt_graph(yaxis_max, json);
            chart.load({
                json: json,
                done: function () {
                    jQuery("#chart").trigger("chart-loading-done");

                }
            });


            chart.axis.max({
                'y': yaxis_max,
                'x': 200
            });

        });
        if (DEBUG_VIEW) {
            jQuery.post(URL_API_PLOT + "?debug_view=true", POST_DATA, function (data) {
                jQuery("#debug_view").html(data);
            });
        }

    };

    $('#institution_type').change(function () {
        $('ui_time_to_graduate').val('');
    });
    $('.form-control').change(change_value);
    $('.bound').change(change_value);
    window.change_default_scenario = function (key, value) {
        if (value === undefined) {
            console.log(default_scenario[key]);
        } else {
            default_scenario[key] = value;
            change_value();
        }

    };
    var sliders = jQuery(".slider");
    for (var i = 0; i < sliders.length; i++) {
        var slider = jQuery(sliders[i]);
        var value_for = slider.data('for');
        var target = jQuery('#' + value_for);
        var min = target.attr('min') !== undefined ? parseInt(target.attr('min')) : 0;
        var max = target.attr('max') !== undefined ? parseInt(target.attr('max')) : 100;
        var step = target.attr('step') !== undefined ? parseFloat(target.attr('step')) : 1.0;
        slider.slider({
            'value': target.val(),
            'min': min,
            'max': max,
            'step': step
        });

    }
    sliders.slider({
        change: function (evnet, ui) {
            change_value();
        },
        slide: function (event, ui) {
            var value_for = jQuery(ui.handle).parent().data('for');
            $("#" + value_for).val(ui.value);
        }
    });

    var options = {
        cell_height: 80,
        vertical_margin: 1,
        static_grid: !('STAFF' in window && STAFF)
    };


    $('.grid-stack').gridstack(options);

    change_value();

    // Fix chart alignment issue
    jQuery("#chart").one('chart-loading-done', function () {
        setTimeout(chart.flush, 100);
    });
});