<!doctype html>
<html>
	<head>
  	<style>
    	html,body{padding:0px;margin:0px;width:100%;height:100%;background: grey;}
        body{display:flex;justify-content:center;align-items:center;}
        main{width:500px;height:500px;padding:20px;border:1px solid grey;background: lightgray;
        border-radius:50px 50px 0px 0px;display:flex;flex-direction:column;justify-content:space-between;}
        input{width:100%;padding:10px;box-sizing:border-box;}
        article{background:lightgreen;padding:20px;border-radius:20px 0px 20px 20px;}
        article.blue{background:lightblue; margin-bottom: 20px;}
    </style>
  </head>
  <body>
  	<main>
    	<section>
        <article class="blue">
            <?php echo $_POST['mensaje'] ?>
        </article>
      	<article>
        	<?php
            $OLLAMA_URL = "http://localhost:11434/api/generate";
            $MODEL = "qwen2.5:3b-instruct";
            $prompt = $_POST['mensaje'].". Responde en español.";
            $data = [
                "model" => $MODEL,
                "prompt" => $prompt,
                "stream" => false
            ];
            $ch = curl_init($OLLAMA_URL);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                "Content-Type: application/json"
            ]);
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
            $response = curl_exec($ch);
            if ($response === false) {
                die("cURL error: " . curl_error($ch));
            }
            curl_close($ch);
            $result = json_decode($response, true);
            echo $result["response"];
          ?>
        </article>
      </section>
      <form action="?" method="POST">
      <input type="text" name="mensaje">
      </form>
    </main>
  </body>
</html>