import re

CHOUSE_REGEXP = re.compile(r'(^\d): ([a-zA-Z]{3,9}),{,(-?\d{1,3}(,{1,2}-?\d{1,3})*,[0-9].[0-9]{1,2})')
EHOUSE_REGEXP = re.compile(
    r'^Elite (\d): ([a-zA-Z]{3,9}),{,(-?\d{1,3}(,{1,3}-?\d{1,3})*,{1,2}-?[0-9]{1,4}.?[0-9]{1,4},)')
BUILDING_REGEXP = re.compile(r'^([0-9]{1,3}),(\b[A-Z]+[_[A-Z]+]*[\d{1,2}]?\b)\s?,{,(-?\d{1,3}[,-?\d{1,3}]*),}')
