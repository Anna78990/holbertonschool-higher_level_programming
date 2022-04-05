#!/usr/bin/node
exports.converter = function (base) {
  return function (v) {
    return v.toString(base);
  };
};
