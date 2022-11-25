export default function Tables() {
  const seed = [
    {nama:'opal',umur:8},
    {nama:'opsal',umur:10},
    {nama:'opdal',umur:80},
    {nama:'opafl',umur:82},

]
  return (
    <>
      <div className="overflow-x-auto relative shadow-md">
        <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
          <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" className="py-3 px-6">
                Nama Depan
              </th>
              <th scope="col" className="py-3 px-6">
                Email
              </th>
              
            </tr>
          </thead>
          <tbody>
            {seed.map((data) => {
              return (
            <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
              <th scope="row" className="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                {data.nama}
              </th>
            <td className="py-4 px-6">{data.umur}</td>

            </tr>
              )})}
          </tbody>
        </table>
      </div>
    </>
  );
}
