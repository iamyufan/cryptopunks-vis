/*export default {
  nodes: [
    {
      name: "Universidad de Granada"
    },
    {
      name: "De Comunidades Autónomas"
    },
    {
      name: "Precios públicos"
    },
    {
      name: "De la Administración General del Estado"
    },
    {
      name: "Ingresos por prestación de servicios"
    },
    {
      name: "Del exterior"
    },
    {
      name: "De la Seguridad Social"
    },
    {
      name: "Tasas"
    },
    {
      name: "De empresas privadas"
    },
    {
      name: "De Organismos Autónomos Administrativos"
    },
    {
      name: "Reintegro de préstamos concedidos"
    },
    {
      name: "Rentas de bienes inmuebles"
    },
    {
      name: "Intereses de depósitos"
    },
    {
      name: "Otros ingresos patrimoniales"
    },
    {
      name: "De empresas públicas y otros entes públicos"
    },
    {
      name: "Venta de bienes"
    },
    {
      name: "De familias e instituciones sin fines de lucro"
    },
    {
      name: "De Corporaciones Locales"
    },
    {
      name: "Otros Ingresos"
    },
    {
      name: "Enseñanzas Universitarias"
    },
    {
      name: "Estructura y Gestión Universitaria"
    },
    {
      name: "Investigación Científica"
    },
    {
      name: "Gastos De Personal"
    },
    {
      name: "Inversiones Reales"
    },
    {
      name: "Gastos En Bienes Corrientes Y Servicios"
    },
    {
      name: "Transferencias Corrientes"
    },
    {
      name: "Activos Financieros"
    },
    {
      name: "Pasivos Financieros"
    },
    {
      name: "Transferencias De Capital"
    },
    {
      name: "Gastos Financieros"
    }
  ],
  links: [
    {
      source: 19,
      target: 26,
      value: 1150000
    },
    {
      source: 0,
      target: 19,
      value: 283175993
    },
    {
      source: 0,
      target: 20,
      value: 64294001
    },
    {
      source: 19,
      target: 22,
      value: 252728897
    },
    {
      source: 20,
      target: 22,
      value: 54659
    },
    {
      source: 21,
      target: 24,
      value: 805940
    },
    {
      source: 19,
      target: 24,
      value: 11754596
    },
    {
      source: 20,
      target: 24,
      value: 25439249
    },
    {
      source: 20,
      target: 29,
      value: 2e5
    },
    {
      source: 21,
      target: 23,
      value: 47161673
    },
    {
      source: 20,
      target: 23,
      value: 36754122
    },
    {
      source: 19,
      target: 23,
      value: 2485000
    },
    {
      source: 0,
      target: 21,
      value: 47967613
    },
    {
      source: 20,
      target: 27,
      value: 1127217
    },
    {
      source: 19,
      target: 25,
      value: 14807500
    },
    {
      source: 20,
      target: 25,
      value: 581754
    },
    {
      source: 20,
      target: 28,
      value: 137000
    },
    {
      source: 19,
      target: 28,
      value: 250000
    },
    {
      source: 1,
      target: 0,
      value: 259498608
    },
    {
      source: 1,
      target: 0,
      value: 30465000
    },
    {
      source: 17,
      target: 0,
      value: 90000
    },
    {
      source: 17,
      target: 0,
      value: 30000
    },
    {
      source: 8,
      target: 0,
      value: 1400000
    },
    {
      source: 8,
      target: 0,
      value: 1275000
    },
    {
      source: 14,
      target: 0,
      value: 4e5
    },
    {
      source: 16,
      target: 0,
      value: 2e5
    },
    {
      source: 3,
      target: 0,
      value: 22245000
    },
    {
      source: 3,
      target: 0,
      value: 10600000
    },
    {
      source: 6,
      target: 0,
      value: 3e6
    },
    {
      source: 5,
      target: 0,
      value: 4e6
    },
    {
      source: 5,
      target: 0,
      value: 3500000
    },
    {
      source: 9,
      target: 0,
      value: 693000
    },
    {
      source: 9,
      target: 0,
      value: 70000
    },
    {
      source: 4,
      target: 0,
      value: 8850000
    },
    {
      source: 12,
      target: 0,
      value: 5e5
    },
    {
      source: 2,
      target: 0,
      value: 44740000
    },
    {
      source: 10,
      target: 0,
      value: 650000
    },
    {
      source: 18,
      target: 0,
      value: 75000
    },
    {
      source: 13,
      target: 0,
      value: 406000
    },
    {
      source: 11,
      target: 0,
      value: 6e5
    },
    {
      source: 7,
      target: 0,
      value: 1900000
    },
    {
      source: 15,
      target: 0,
      value: 250000
    }
  ]
};
*/

export default {
  nodes: [
    { name: "A", color: "red" },
    { name: "B", color: "yellow" },
    { name: "C", color: "blue" },
    // level 2
    { name: "D", color: "green" },
    { name: "E", color: "purple" },
    // level 3
    { name: "F", color: "cyan" },
    { name: "G", color: "yellow" },
    // level 4
    { name: "H", color: "red" },
    { name: "I", color: "blue" },
  ],
  links: [
    { source: "A", target: "D", value: Math.random() * 100 },
    { source: "A", target: "E", value: Math.random() * 100 },
    { source: "B", target: "D", value: Math.random() * 100 },
    { source: "B", target: "E", value: Math.random() * 100 },
    { source: "C", target: "E", value: Math.random() * 100 },
    { source: "D", target: "F", value: Math.random() * 100 },
    { source: "D", target: "G", value: Math.random() * 100 },
    { source: "E", target: "G", value: Math.random() * 100 },
    { source: "F", target: "H", value: Math.random() * 100 },
    { source: "F", target: "I", value: Math.random() * 100 },
    { source: "G", target: "H", value: Math.random() * 100 },
    { source: "G", target: "I", value: Math.random() * 100 },
  ],
  units: "TWh",
};
