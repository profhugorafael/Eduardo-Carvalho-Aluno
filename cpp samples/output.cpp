  // input and output stream
  #include <iostream> 
  #include <string>

  // coloco no modo standard
  using namespace std;

  // crio meu entrypoint
  int main(){
    
    cout << "Digite uma frase: ";

    string frase;
    getline(cin, frase);

    cout << "Hello World!" << endl;
    // command out
    // endline

    return 0;
    // forço a parada do programa
  }