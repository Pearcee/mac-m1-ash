var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var formatDate = function (date) {
    return date.getHours() + ":" + String(date.getMinutes()).padStart(2, '0') + " " + String(date.getSeconds()).padStart(2, '0') + "." + String(date.getMilliseconds()).padStart(3, '0');
};
function fetchPokemon(name) {
    var _a;
    return __awaiter(this, void 0, void 0, function () {
        var pokemonQuery, response, _b, data, errors, pokemon, error;
        return __generator(this, function (_c) {
            switch (_c.label) {
                case 0:
                    pokemonQuery = "\n    query PokemonInfo($name: String) {\n      pokemon(name: $name) {\n        id\n        number\n        name\n        image\n        attacks {\n          special {\n            name\n            type\n            damage\n          }\n        }\n      }\n    }\n  ";
                    return [4 /*yield*/, window.fetch('https://graphql-pokemon2.vercel.app/', {
                            // learn more about this API here: https://graphql-pokemon2.vercel.app/
                            method: 'POST',
                            headers: {
                                'content-type': 'application/json;charset=UTF-8'
                            },
                            body: JSON.stringify({
                                query: pokemonQuery,
                                variables: { name: name.toLowerCase() }
                            })
                        })];
                case 1:
                    response = _c.sent();
                    return [4 /*yield*/, response.json()];
                case 2:
                    _b = _c.sent(), data = _b.data, errors = _b.errors;
                    if (response.ok) {
                        pokemon = data === null || data === void 0 ? void 0 : data.pokemon;
                        if (pokemon) {
                            // add fetchedAt helper (used in the UI to help differentiate requests)
                            return [2 /*return*/, Object.assign(pokemon, { fetchedAt: formatDate(new Date()) })];
                        }
                        else {
                            return [2 /*return*/, Promise.reject(new Error("No pokemon with the name \"" + name + "\""))];
                        }
                    }
                    else {
                        error = new Error((_a = errors === null || errors === void 0 ? void 0 : errors.map(function (e) { return e.message; }).join('\n')) !== null && _a !== void 0 ? _a : 'unknown');
                        return [2 /*return*/, Promise.reject(error)];
                    }
                    return [2 /*return*/];
            }
        });
    });
}
