<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Annotation\Route;

/**
 * Description of AccueilController
 *
 * @Route ("/Acceuil", name="Accueil")
 * @return Response
 */
class AccueilController extends AbstractController{
    public function index(): Response{
        $jsonFilePath = $this->getParameter('kernel.project_dir') . '/public/json/data.json';
        $datas = json_decode(file_get_contents($jsonFilePath), true);
        return $this->render("pages/index.html.twig", array(
            "datas" => $datas,
        ));
    }

    /**
     * @Route("/filter_byfirstname", name="filter_byfirstname")
     */
    public function filter_byfirstname(Request $request): JsonResponse
    {
        $jsonFilePath = $this->getParameter('kernel.project_dir') . '/public/json/data.json';
        $datas = json_decode(file_get_contents($jsonFilePath), true);

        $filter = $request->query->get('filter');
        $filteredData = array_filter($datas, function($item) use ($filter) {
            return stripos($item['prenom'], $filter) !== false;
        });

        return new JsonResponse(array_values($filteredData));
    }

    /**
     * @Route("/filter_byname", name="filter_byname")
     */
    public function filter_byname(Request $request): JsonResponse
    {
        $jsonFilePath = $this->getParameter('kernel.project_dir') . '/public/json/data.json';
        $datas = json_decode(file_get_contents($jsonFilePath), true);

        $filter = $request->query->get('filter');
        $filteredData = array_filter($datas, function($item) use ($filter) {
            return stripos($item['nom'], $filter) !== false;
        });

        return new JsonResponse(array_values($filteredData));
    } 
    
    /**
    * @Route("/filter_bymail", name="filter_bymail")
    */
   public function filter_bymail(Request $request): JsonResponse
   {
       $jsonFilePath = $this->getParameter('kernel.project_dir') . '/public/json/data.json';
       $datas = json_decode(file_get_contents($jsonFilePath), true);

       $filter = $request->query->get('filter');
       $filteredData = array_filter($datas, function($item) use ($filter) {
           return stripos($item['email'], $filter) !== false;
       });

       return new JsonResponse(array_values($filteredData));
   }
}
?>