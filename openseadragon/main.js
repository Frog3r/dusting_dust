const options =  {
    id: 'container',
    prefixUrl : 'https://cdnjs.cloudflare.com/ajax/libs/openseadragon/5.0.1/images/',
    collectionMode : true,
    tileSources: [
        {
            type: 'image',
            url: 'https://images.pexels.com/photos/33045/lion-wild-africa-african.jpg'
        },
        {
         type: 'image',
         url: 'https://images.unsplash.com/photo-1517036391698-b004444390fe?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'   
        }
    ]
};2
const viewer = OpenSeadragon(options);