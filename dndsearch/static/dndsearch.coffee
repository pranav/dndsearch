# DndSearch

dndSearchApp = angular.module 'dndSearchApp', []

dndSearchApp.controller 'MainCtrl', ['$scope', '$http', ($scope, $http) ->
  $scope.results = []

  $scope.submit_query = (query) ->
    $http.get("/query/#{query}").success (results) ->
      if results.length == 0
        $scope.results = [{'book': 'Sorry no results were found', 'page': ''}]
      else
        $scope.results = results
]

