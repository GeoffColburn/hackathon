/**
 * Created by geoffc on 8/13/14.
 */
var hackFilters = angular.module('hackFilters', []);

hackFilters.filter('joinTags', function () {
    return function (input, delimiter) {
        if (input === undefined) {
            return '';
        }
        input = input.map(function (x) {
            return x.text
        });
        return (input || []).join(delimiter || ',');
    };
});

hackFilters.filter('joinSkills', function () {
    var map = {
        illustrator: 'Illustrator',
        webdesigner: 'Web-Designer',
        editor: 'Editor',
        videographer: 'Videographer',
        photographer: 'Photographer',
        writer: 'Writer'
    }
    return function (input, delimiter) {
        if (input === undefined) {
            return '';
        }
        console.dir(input);
        var tokens = [];
        $.each(input, function(k,v) {
            if (v === true) {
                tokens.push(map[k]);
            }
        });

        return (tokens || []).join(delimiter || ',');
    };
});