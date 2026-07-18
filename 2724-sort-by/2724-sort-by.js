/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
  return sortedArr = arr.toSorted((a,b)=> fn(a) - fn(b))  
};