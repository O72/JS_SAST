const crypto = require("crypto");
function hash_sha1(hash) {
    var hasher = crypto.createHash('sha1');
    var hashed = hasher.update(hash).digest("hex"); // BAD
    return hashed;
}

