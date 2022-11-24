function myMethod(foo) {
    console.log(foo + ": " + eval(foo));
}
export function unsafeDeserialize(value) {
  return eval(`(${value})`);
}

export function unsafeGetter(obj, path) {
    return eval(`obj.${path}`);
}