var myApp = angular.module('myApp', [])


.controller('TabsCtrl', ['$scope', function ($scope) {
    
    $scope.tabs = [{

            title: 'Home',
            url: 'home.tmpl.html'

        }, {

            title: 'Calendar',
            url: 'cal.tmpl.html'

        }, {
            title: 'Video',
            url: 'video.tmpl.html'
    }];

    $scope.currentTab = 'home.tmpl.html';

    $scope.onClickTab = function (tab) {
        $scope.currentTab = tab.url;
    }
    $scope.isActiveTab = function(tabUrl) {
        return tabUrl == $scope.currentTab;
    }
}]);
