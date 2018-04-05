Feature: User can search Amazon for products

  Scenario: Search for blenders
     Given we are browsing amazon.com
      When we search for "blender"
      Then we should see a " Blender "

  Scenario: Search for mowers
     Given we are browsing amazon.com
      When we search for "mower"
      Then we should see a " Mower "

