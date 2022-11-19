const crypto = require("crypto");
function hash_md5(hash) {
    var hasher = crypto.createHash('md5');
    var hashed = hasher.update(hash).digest("hex"); // BAD
    return hashed;
}
